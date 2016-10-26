import React from 'react';
import {render} from 'react-dom';
import ReactDOM from 'react-dom';
import Highlighter from 'react-highlight-words'
import update from 'immutability-helper'
import Base from './base'
import Lightbox from 'react-images'

var fetchWithAuth = Base.fetchWithAuth

console.log(fetchWithAuth);

var config = {
    container: document.getElementsByClassName('b-feed')[0],
    api_client_id: 'K3mguv60CF2T8Oq7icUff2PQLLKjNDUrgvEUuQpx'
}

console.log(config);

class Comment extends React.Component {
    state = {
    }

    getUser(pk) {
        if (this.state.user) {
            return;
        }
        let _this = this;
        fetchWithAuth('/api/v1/user/' + pk.toString() + '/')
            .then(function(response) {
                response.json().then((data) => {
                    _this.setState({user: data["user"],});
                });
            });
    }

    render() {
        this.getUser(this.props.user);
        return (
            <div>
                <b> {this.state.user} </b>

                <p> {this.props.text} </p>
                <div className="pull-right"> Likes: {this.props.likes_count} </div>
                <br />

            </div>
        )
    }
}

class Post extends React.Component {
    state = {
        attachments: {},
        comments: [],
        comments_collapsed: true,
    }

    comments_fetched = false;

    getAttachmentUrl(pk) {
        if (this.state.attachments[pk]) {
            return;
        }

        let _this = this;
        fetchWithAuth('/api/v1/image/' + pk.toString() + '/')
            .then(function(response) {
                return response.json().then((data) => {
                    _this.setState({
                        attachments:
                            update(_this.state.attachments,
                                   { [pk]: {$set: data["url"]}}),
                    });
                });
            });
    }

    getUser(pk) {
        if (this.state.user) {
            return;
        }
        let _this = this;
        fetchWithAuth('/api/v1/user/' + pk.toString() + '/')
            .then(function(response) {
                response.json().then((data) => {
                    _this.setState({user: data["user"],});
                });
            });
    }

    getComments() {
        if (this.comments_fetched) {
            return;
        }
        this.comments_fetched = true;
        let _this = this;
        fetchWithAuth('/api/v1/comment/?item_id='
                      + _this.props.pk.toString()
                      + "&item_type=post").then((response) => {
                          response.json().then((data) => {
                              _this.setState({comments: data["results"],});
                          });
                      });
    }

    toggleComments() {
        if (this.state.comments_collapsed) {
            this.getComments();
            this.setState({comments_collapsed: false});
        } else {
            this.setState({comments_collapsed: true});
        }
    }



    render() {
        this.props.attachments.forEach(this.getAttachmentUrl.bind(this));
        this.getUser(this.props.user);
        return (
            <div>
                <div className="row">
                  <div className="col-sm-12">
                    <div className="">
                     <h1>{this.state.user ? this.state.user : ''}</h1>
                     <p><small>{ this.props.created_at } </small></p>

                     {/* <img src="http://chocolatevent.by/sites/default/files/noavatar.png" className="img-circle" height="55" width="55" alt="Avatar" /> */}
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-sm-12">
                    <div className="">
                      <div>
                        <Highlighter highlightClassName='Highlight' searchWords={ [this.props.highlight] } style={ {whiteSpace: 'pre-wrap', textAlign: 'left'} } textToHighlight={ this.props.text }/>
                      </div>

                      {Object.keys(this.state.attachments).map((item) => <img className="img-thumbnail" style={ {maxHeight: "55px"} } key={item} src={this.state.attachments[item]} />)}

                      <p className="pull-right">
                        Likes: { this.props.likes_count }
                      </p>
                    </div>
                    <br />
                    <div className="">
                        <button type="button"className="btn btn-primary btn-sm btn-block" onClick={this.toggleComments.bind(this)}>
                            {this.state.comments_collapsed ?  <p>Expand Comments ({this.props.comments_count})</p> : <p>Collapse Comments ({this.props.comments_count})</p>}
                        </button>
                    </div>
                    {
                        this.state.comments_collapsed ? <div></div> :
                        <div>
                            {this.state.comments.map((item) => <Comment key={item.pk} {...item}/>)}
                        </div>
                    }
                    <hr />
                  </div>
                </div>
            </div>
        )
    }
}

class PostList extends React.Component {
    state = {
        objects : [],
        q: '',
    }

    inited = false;

    searchFieldChanged(e) {
        this.loadDataFromServer(e.target.value);
    }

    loadDataFromServer(q='') {
        window.location.hash = q;
        let _this = this
        fetchWithAuth('/api/v1/post/?q=' + encodeURIComponent(q)).then(function(response) {
                if (response.status)
                response.json().then(function(data) {
                    _this.setState({objects: data.results, q: q});
                })
            }).catch(function(err) {
                console.log(err);
            })
    }

    render() {
        if (!this.inited) {
            this.inited =  true;
            this.loadDataFromServer(window.location.hash.slice(1,));
        }
        console.log(this.state.objects)
        return (
            <div className="row">
                <div className="col-sm-12" >
                    <input type="text" className="form-control" onInput={this.searchFieldChanged.bind(this)} value={window.location.hash.slice(1,)} placeholder="Search.." />
                </div>
                {this.state.objects.map((item) => <Post key={item.pk} highlight={this.state.q} {...item} />)}
            </div>
        )
    }
}

ReactDOM.render(
    <PostList />,
    config.container
)

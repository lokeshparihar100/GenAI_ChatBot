css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

dashboard_css = '''
<style>

[data-testid="stAppViewContainer"] {
background: #dbe4ff;
}

:root {
    --primary: #3b5bdb;
    --secondary: #dbbb3b;
  }

.wrapper {
    margin: 40px auto;
    width: 1000px;
}

h1 {
  margin: 10px;
  color: var(--primary);
  text-decoration: none;
}

.grid-wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
}

.grid {
  height: 200px;
  border-color: #3b5bdb;
  background-color: #fff;
  border: 2px solid #748ffc;
  padding: 5px;
  margin: 10px;
  border-radius: 10px;
  position: relative;
  &:hover {
    .grid-overlay {
      transform: translate(0, 0);
      opacity: 1;
      visibility: visible;

      .overlay-header {
        transform: translate(0, 0);
        opacity: 1;
        visibility: visible;
        &:before {
          transform: translate(0, 0);
          opacity: 1;
          visibility: visible;
        }
      }
    }
  }
}
.grid-header {
  height: 90%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  font-size: 30px;
  &:hover {
    cursor: pointer;
  }

  .icon {
    color: #333;
    font-size: 50px;
  }

  .label {
    color: var(--primary);
    margin-top: 10px;
  }
}
.grid-overlay {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: rgba(59, 91, 219, 0.95);
  overflow: hidden;
  cursor: pointer;
  border-radius: 10px;
  border: 2px solid transparent;
  transform: translate(-10%, 0);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.5s ease-in-out, transform 0.7s ease-in-out;
}
.overlay-content-wrapper {
  width: 100%;
  height: 100%;
  padding: 20px;
  color: var(--secondary);

  .overlay-header {
    font-size: 25px;
    margin-bottom: 25px;
    position: relative;
    transform: translatex(-70px);
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.5s ease-in-out 0.4s, transform 0.7s ease-in-out 0.4s;
    &:before {
      content: "";
      position: absolute;
      bottom: -10px;
      width: 40px;
      height: 3px;
      background-color: var(--secondary);
      transform: translatey(20px);
      opacity: 0;
      visibility: hidden;

      transition: opacity 0.3s ease-in-out 0.8s, transform 0.2s ease-in-out 0.7s;
    }
  }
}
.user-grid {
  border: 0;
  .label {
    color: #222;
    font-size: 22px;
  }
}
.overlay-label {
  font-size: 14px;
  line-height: 1.3;
  word-spacing: 2px;
}
.author {
  color: black;
  text-align: center;
  font-weight: 600;
  margin-top: 30px;
  font-size: 22px;
}
'''

dashboard_html = '''

<div class="wrapper">
    <h1>Dashboard</h1>
<div class="grid-wrapper">

<a href="/QA_on_Pdfs_📚" target="_self"> 
<div class="grid">
<div class="grid-header"> 
<div class="icon">
    <i class="fa fa-user" aria-hidden="true"></i>
</div>    
<div class="label">
<h1> PDFs </h1>
</div></div>
<div class="grid-overlay">
<div class="overlay-content-wrapper">
<div class="overlay-header">PDF</div>
 <div class="overlay-label">
Upload a single or multiple PDFs and ask your questions.
</div></div></div></div></a>

<a href="/QA_on_Web_🌐" target="_self">
<div class="grid">
<div class="grid-header"> 
<div class="icon">
    <i class="fa fa-user" aria-hidden="true"></i>
</div>  
<div class="label">
<h1> Web </h1>
</div></div>
<div class="grid-overlay">
<div class="overlay-content-wrapper">
<div class="overlay-header">Web</div>
 <div class="overlay-label">
Enter a website link and ask your questions.
</div></div></div></div></a>

<a href="/QA_on_Image_📷" target="_self">
<div class="grid">
<div class="grid-header">
<div class="icon">
    <i class="fa fa-user" aria-hidden="true"></i>
</div> 
<div class="label">
<h1> Image </h1>
</div></div>
<div class="grid-overlay">
<div class="overlay-content-wrapper">
<div class="overlay-header">Image</div>
<div class="overlay-label">
Upload a Image and ask your questions.
</div></div></div></div></a>

<a href="/QA_on_Video_🎬" target="_self">
<div class="grid">
<div class="grid-header">
<div class="icon">
    <i class="fa fa-user" aria-hidden="true"></i>
</div> 
<div class="label">
<h1>  Video </h1>
</div></div>
<div class="grid-overlay">
<div class="overlay-content-wrapper">
<div class="overlay-header">Video</div>
 <div class="overlay-label">
Upload a video or video link and ask your questions.
</div></div></div></div></a>

<div class="author">
    A project by Jaipur Jaguars <img width="50" height="50" src="https://img.icons8.com/bubbles/50/jaguar.png" alt="jaguar"/>
</div>
</div>
</div>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img width="50" height="50" src="https://img.icons8.com/arcade/64/bot.png" alt="bot"/>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img width="40" height="40" src="https://img.icons8.com/officel/40/user.png" alt="user"/>
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

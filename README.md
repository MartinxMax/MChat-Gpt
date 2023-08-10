  <div align="center">
<p align="center">
 <img title="GPT" src='https://img.shields.io/badge/MChat-Gpt-1.0.0-brightgreen.svg' />
 <img title="GPT" src='https://img.shields.io/badge/Python-3.9-yellow.svg' />
  <img title="GPT" src='https://img.shields.io/badge/HackerTool-x' />
 <img title="GPT" src='https://img.shields.io/static/v1?label=Author&message=@Martin&color=red'/>
 <img title="GPT" src='https://img.shields.io/badge/-windows-F16061?logo=windows&logoColor=000'/>
<img title="GPT" src='https://img.shields.io/badge/-Linux-F16061?logo=Linux&logoColor=000'/>
 
</p>
  
   
 <table>
  <tr>
      <th>Function</th>
  </tr>
  <tr>
    <th>Calling the chatgpt interface to achieve data sharing between internal and external networks</th>
</tr>
 
 </table>
</div>


!!Please set your agent to TUN mode!!

  
## Chatgpt Example

``Choose your operating system installation``


![图片名称](./PT/1.png) 

## Server Example

``#python3 ChatGpt_Server.py -h``

![图片名称](./PT/2.png) 

*Use (-pf) for data sharing and open ports for other hosts to query(If not filled in, it will be for personal use)*

``_You can use - lp to customize the port, default to 10032_``

``#python3 ChatGpt_Server.py -pf -lp 10034``

![图片名称](./PT/3.png) 

![图片名称](./PT/6.png) 

## Client Example


``#python3 ChatGpt_Server.py -h``

![图片名称](./PT/4.png) 


``#python3 ChatGpt_Server.py -rh 192.168.8.104:10034``

![图片名称](./PT/5.png) 


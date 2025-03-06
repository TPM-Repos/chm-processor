SendMessageToUser(String,MessageBoxIcon,String) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IInteraction Interface](topic321.md) > [SendMessageToUser Method](topic329.md) : SendMessageToUser(String,MessageBoxIcon,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message to send.

_icon_
    The icon shown in the message box.

_helpTopic_
    A help topic to be shown if the user requests help.

Glossary Item Box

Sends a message to the user of the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Sub SendMessageToUser( _
       ByVal _message_ As String, _
       ByVal _icon_ As MessageBoxIcon, _
       ByVal _helpTopic_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IInteraction](topic321.md)
    Dim message As String
    Dim icon As MessageBoxIcon
    Dim helpTopic As String
     
    instance.SendMessageToUser(message, icon, helpTopic)  
  
C#|   
---|---  
      
    
    void SendMessageToUser( 
       string _message_ ,
       MessageBoxIcon _icon_ ,
       string _helpTopic_
    )  
  
#### Parameters

 _message_
    The message to send.
_icon_
    The icon shown in the message box.
_helpTopic_
    A help topic to be shown if the user requests help.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IInteraction Interface](topic321.md)   
[IInteraction Members](topic322.md)   
[Overload List](topic329.md)



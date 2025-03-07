Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AgentRequestReceived Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : AgentRequestReceived Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a request is received from another session. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event AgentRequestReceived As EventHandler(Of RequestEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim handler As EventHandler(Of RequestEventArgs)
     
    AddHandler instance.AgentRequestReceived, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<RequestEventArgs> AgentRequestReceived  
  
# Event Data

The event handler receives an argument of type [RequestEventArgs](topic10071.md) containing data related to this event. The following **RequestEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Message](topic10077.md)| Gets the request message.   
[ReplyMessageData](topic10078.md)| Gets/sets the reply message to send back to the sender of this request.   
  
# Remarks

Replies are completed through the event args and can only be replied to once. Once a reply has been made no other listeners to this event will receive an invocation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)



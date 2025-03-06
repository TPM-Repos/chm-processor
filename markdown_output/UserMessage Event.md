UserMessage Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IUserMessageService Interface](topic526.md) : UserMessage Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a new user message is received. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event UserMessage As EventHandler(Of UserMessageEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IUserMessageService](topic526.md)
    Dim handler As EventHandler(Of UserMessageEventArgs)
     
    AddHandler instance.UserMessage, handler  
  
C#|   
---|---  
      
    
    event EventHandler<UserMessageEventArgs> UserMessage  
  
# Event Data

The event handler receives an argument of type [UserMessageEventArgs](topic5827.md) containing data related to this event. The following **UserMessageEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Message](topic5833.md)|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IUserMessageService Interface](topic526.md)   
[IUserMessageService Members](topic527.md)



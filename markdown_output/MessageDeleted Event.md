Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MessageDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMessages Class](topic4627.md) : MessageDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the message is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event MessageDeleted As [MessageChangedEventHandler](topic5932.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectMessages](topic4627.md)
    Dim handler As [MessageChangedEventHandler](topic5932.md)
     
    AddHandler instance.MessageDeleted, handler  
  
C#|   
---|---  
      
    
    public event [MessageChangedEventHandler](topic5932.md) MessageDeleted  
  
# Event Data

The event handler receives an argument of type [MessageEventArgs](topic3704.md) containing data related to this event. The following **MessageEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Message](topic3714.md)| Gets the message that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMessages Class](topic4627.md)   
[ProjectMessages Members](topic4628.md)



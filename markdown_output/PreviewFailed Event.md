Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviewFailed Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewControl Class](topic8709.md) : PreviewFailed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Event for when model generation fails. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event PreviewFailed As [PreviewControl.PreviewFailedEventHandler](topic9368.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PreviewControl](topic8709.md)
    Dim handler As [PreviewControl.PreviewFailedEventHandler](topic9368.md)
     
    AddHandler instance.PreviewFailed, handler  
  
C#|   
---|---  
      
    
    public event [PreviewControl.PreviewFailedEventHandler](topic9368.md) PreviewFailed  
  
# Event Data

The event handler receives an argument of type [PreviewExceptionEventArgs](topic3811.md) containing data related to this event. The following **PreviewExceptionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Exception](topic3818.md)| Gets the exception to which the event refers.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreviewControl Class](topic8709.md)   
[PreviewControl Members](topic8710.md)



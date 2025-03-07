Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IncludeFileFormatsInLoopChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ProjectComponent Class](topic6183.md) : IncludeFileFormatsInLoopChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever the [IncludeFileFormatsInLoop](topic6192.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event IncludeFileFormatsInLoopChanged As EventHandler(Of ValueChangedEventArgs(Of Boolean))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponent](topic6183.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs(Of Boolean))
     
    AddHandler instance.IncludeFileFormatsInLoopChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueChangedEventArgs<bool>> IncludeFileFormatsInLoopChanged  
  
# Event Data

The event handler receives an argument of type [ValueChangedEventArgs<T>](topic5834.md) containing data related to this event. The following **ValueChangedEventArgs <T>** properties provide information specific to this event.

Property| Description  
---|---  
[NewValue](topic5841.md)| Gets the new value.   
[OldValue](topic5842.md)| Gets the old value.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponent Class](topic6183.md)   
[ProjectComponent Members](topic6184.md)



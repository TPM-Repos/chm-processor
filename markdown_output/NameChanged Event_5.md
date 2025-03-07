Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NameChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSet Class](topic4106.md) : NameChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the component set's name changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NameChanged As EventHandler(Of NameChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSet](topic4106.md)
    Dim handler As EventHandler(Of NameChangedEventArgs)
     
    AddHandler instance.NameChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<NameChangedEventArgs> NameChanged  
  
# Event Data

The event handler receives an argument of type DriveWorks.Support.NameChangedEventArgs containing data related to this event. The following **NameChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
**NewName**|   
**OldName**|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSet Class](topic4106.md)   
[ProjectComponentSet Members](topic4107.md)



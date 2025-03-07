Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NameValueChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : NameValueChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the name of the control changes and provides information on the name change (Old name and new name). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NameValueChanged As EventHandler(Of NameChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim handler As EventHandler(Of NameChangedEventArgs)
     
    AddHandler instance.NameValueChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<NameChangedEventArgs> NameValueChanged  
  
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

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)



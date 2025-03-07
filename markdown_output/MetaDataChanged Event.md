Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MetaDataChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupDataTable Class](topic3110.md) : MetaDataChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the metadata of this table changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event MetaDataChanged As EventHandler(Of ValueChangedEventArgs(Of String))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupDataTable](topic3110.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs(Of String))
     
    AddHandler instance.MetaDataChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueChangedEventArgs<string>> MetaDataChanged  
  
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

[GroupDataTable Class](topic3110.md)   
[GroupDataTable Members](topic3111.md)



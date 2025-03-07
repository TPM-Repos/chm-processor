Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OldSelectedItems Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SelectionChangeEventArgs Class](topic926.md) : OldSelectedItems Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the selection before the change took place. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property OldSelectedItems As Object()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SelectionChangeEventArgs](topic926.md)
    Dim value() As Object
     
    value = instance.OldSelectedItems  
  
C#|   
---|---  
      
    
    public object[] OldSelectedItems {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SelectionChangeEventArgs Class](topic926.md)   
[SelectionChangeEventArgs Members](topic927.md)



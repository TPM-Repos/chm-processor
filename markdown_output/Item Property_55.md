Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocumentRules Class](topic4413.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the document rule to retrieve.

Glossary Item Box

Gets the document rule at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectDocumentRule](topic4399.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocumentRules](topic4413.md)
    Dim index As Integer
    Dim value As [ProjectDocumentRule](topic4399.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectDocumentRule](topic4399.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the document rule to retrieve.

#### Property Value

The document rule at the specified index.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocumentRules Class](topic4413.md)   
[ProjectDocumentRules Members](topic4414.md)



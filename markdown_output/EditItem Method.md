Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EditItem Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : EditItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_itemIndex_
    The row index of the item to edit.

_specificationName_
    The new name of the specification that was edited.

_values_
    New values for the item.

Glossary Item Box

Edits an existing item in this item list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub EditItem( _
       ByVal _itemIndex_ As Integer, _
       ByVal _specificationName_ As String, _
       ByVal _values_() As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim itemIndex As Integer
    Dim specificationName As String
    Dim values() As Object
     
    instance.EditItem(itemIndex, specificationName, values)  
  
C#|   
---|---  
      
    
    public void EditItem( 
       int _itemIndex_ ,
       string _specificationName_ ,
       object[] _values_
    )  
  
#### Parameters

 _itemIndex_
    The row index of the item to edit.
_specificationName_
    The new name of the specification that was edited.
_values_
    New values for the item.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)



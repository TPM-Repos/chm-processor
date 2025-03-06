       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SpecificationMacroCategory Class](topic5359.md) : TryGetCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the category to get.

_itemCategory_
    Receives the named category if it was found, otherwise receives a null reference (Nothing in Visual Basic).

Glossary Item Box

Tries to get a category with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetCategory( _
       ByVal _name_ As String, _
       ByRef _itemCategory_ As [SpecificationMacroCategory](topic5359.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacroCategory](topic5359.md)
    Dim name As String
    Dim itemCategory As [SpecificationMacroCategory](topic5359.md)
    Dim value As Boolean
     
    value = instance.TryGetCategory(name, itemCategory)  
  
C#|   
---|---  
      
    
    public bool TryGetCategory( 
       string _name_ ,
       ref [SpecificationMacroCategory](topic5359.md) _itemCategory_
    )  
  
#### Parameters

 _name_
    The name of the category to get.
_itemCategory_
    Receives the named category if it was found, otherwise receives a null reference (Nothing in Visual Basic).

#### Return Value

True if the named category was found, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacroCategory Class](topic5359.md)   
[SpecificationMacroCategory Members](topic5360.md)



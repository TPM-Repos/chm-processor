TryGetCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SpecificationMacroCategories Class](topic5342.md) : TryGetCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the category to retrieve.

_category_
    A reference to a Project Category which will received the category.

Glossary Item Box

Gets the named category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetCategory( _
       ByVal _name_ As String, _
       ByRef _category_ As [SpecificationMacroCategory](topic5359.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacroCategories](topic5342.md)
    Dim name As String
    Dim category As [SpecificationMacroCategory](topic5359.md)
    Dim value As Boolean
     
    value = instance.TryGetCategory(name, category)  
  
C#|   
---|---  
      
    
    public bool TryGetCategory( 
       string _name_ ,
       ref [SpecificationMacroCategory](topic5359.md) _category_
    )  
  
#### Parameters

 _name_
    The name of the category to retrieve.
_category_
    A reference to a Project Category which will received the category.

#### Return Value

True if the specified project category was found, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacroCategories Class](topic5342.md)   
[SpecificationMacroCategories Members](topic5343.md)



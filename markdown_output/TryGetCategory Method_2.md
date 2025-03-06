       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariableCategories Class](topic4966.md) : TryGetCategory Method  
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
       ByRef _category_ As [ProjectVariableCategory](topic4983.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariableCategories](topic4966.md)
    Dim name As String
    Dim category As [ProjectVariableCategory](topic4983.md)
    Dim value As Boolean
     
    value = instance.TryGetCategory(name, category)  
  
C#|   
---|---  
      
    
    public bool TryGetCategory( 
       string _name_ ,
       ref [ProjectVariableCategory](topic4983.md) _category_
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

[ProjectVariableCategories Class](topic4966.md)   
[ProjectVariableCategories Members](topic4967.md)



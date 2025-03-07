Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariableCategories Class](topic4966.md) : CreateCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the new category which must be unique in the current scope.

Glossary Item Box

Creates a new project category with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateCategory( _
       ByVal _name_ As String _
    ) As [ProjectVariableCategory](topic4983.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariableCategories](topic4966.md)
    Dim name As String
    Dim value As [ProjectVariableCategory](topic4983.md)
     
    value = instance.CreateCategory(name)  
  
C#|   
---|---  
      
    
    public [ProjectVariableCategory](topic4983.md) CreateCategory( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the new category which must be unique in the current scope.

#### Return Value

The newly created project category.

# Exceptions

Exception| Description  
---|---  
[ItemExistsException](topic3561.md)| Thrown if a category with the specified name already exists in the current scope.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariableCategories Class](topic4966.md)   
[ProjectVariableCategories Members](topic4967.md)



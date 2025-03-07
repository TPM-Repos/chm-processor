Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCategoryByPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariableCategories Class](topic4966.md) : GetCategoryByPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_path_
    The full path to the category, delimited with the backslash character.

Glossary Item Box

Gets the category with the specified path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetCategoryByPath( _
       ByVal _path_ As String _
    ) As [ProjectVariableCategory](topic4983.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariableCategories](topic4966.md)
    Dim path As String
    Dim value As [ProjectVariableCategory](topic4983.md)
     
    value = instance.GetCategoryByPath(path)  
  
C#|   
---|---  
      
    
    public [ProjectVariableCategory](topic4983.md) GetCategoryByPath( 
       string _path_
    )  
  
#### Parameters

 _path_
    The full path to the category, delimited with the backslash character.

#### Return Value

The found category or nothing if it could not be found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariableCategories Class](topic4966.md)   
[ProjectVariableCategories Members](topic4967.md)



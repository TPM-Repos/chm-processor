Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariableCategories Class](topic4966.md) : GetCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the category to retrieve.

Glossary Item Box

Gets the named category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetCategory( _
       ByVal _name_ As String _
    ) As [ProjectVariableCategory](topic4983.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariableCategories](topic4966.md)
    Dim name As String
    Dim value As [ProjectVariableCategory](topic4983.md)
     
    value = instance.GetCategory(name)  
  
C#|   
---|---  
      
    
    public [ProjectVariableCategory](topic4983.md) GetCategory( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the category to retrieve.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown if the specified category is not found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariableCategories Class](topic4966.md)   
[ProjectVariableCategories Members](topic4967.md)



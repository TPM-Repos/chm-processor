Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstantCategory Class](topic4219.md) : GetCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the category to get.

Glossary Item Box

Gets the child project category with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetCategory( _
       ByVal _name_ As String _
    ) As [ProjectConstantCategory](topic4219.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstantCategory](topic4219.md)
    Dim name As String
    Dim value As [ProjectConstantCategory](topic4219.md)
     
    value = instance.GetCategory(name)  
  
C#|   
---|---  
      
    
    public [ProjectConstantCategory](topic4219.md) GetCategory( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the category to get.

#### Return Value

The named category.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown when the specified category is not found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstantCategory Class](topic4219.md)   
[ProjectConstantCategory Members](topic4220.md)



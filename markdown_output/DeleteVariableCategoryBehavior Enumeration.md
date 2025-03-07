Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteVariableCategoryBehavior Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : DeleteVariableCategoryBehavior Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies the behavior to use when deleting a variable category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum DeleteVariableCategoryBehavior 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DeleteVariableCategoryBehavior](topic2351.md)  
  
C#|   
---|---  
      
    
    public enum DeleteVariableCategoryBehavior : System.Enum   
  
# Members

Member| Description  
---|---  
**DeleteCategoriesAndMoveVariables**|  Deletes descendent categories, and moves all descendent variables to the category's parent.  
**MoveCategoriesAndVariables**|  Moves child categories and variables to the category's parent.  
**None**|  Delete a single variable category with no children.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.DeleteVariableCategoryBehavior**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks Namespace](topic2159.md)



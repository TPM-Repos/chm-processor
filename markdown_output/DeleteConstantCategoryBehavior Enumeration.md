Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteConstantCategoryBehavior Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : DeleteConstantCategoryBehavior Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies the behaviour to use when deleting a constant category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum DeleteConstantCategoryBehavior 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DeleteConstantCategoryBehavior](topic2349.md)  
  
C#|   
---|---  
      
    
    public enum DeleteConstantCategoryBehavior : System.Enum   
  
# Members

Member| Description  
---|---  
**DeleteCategoriesAndMoveConstants**|  Deletes descendent categories, and moves all descendent constants to the category's parent.  
**MoveCategoriesAndConstants**|  Moves child categories and constants to the category's parent.  
**None**|  Delete a single constant category with no children.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.DeleteConstantCategoryBehavior**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks Namespace](topic2159.md)



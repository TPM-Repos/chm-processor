Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteMacroCategoryBehavior Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : DeleteMacroCategoryBehavior Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies the behavior to use when deleting a specification macro category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum DeleteMacroCategoryBehavior 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DeleteMacroCategoryBehavior](topic2350.md)  
  
C#|   
---|---  
      
    
    public enum DeleteMacroCategoryBehavior : System.Enum   
  
# Members

Member| Description  
---|---  
**DeleteCategoriesAndMoveMacros**|  Deletes descendent categories, and moves all descendent macros to the category's parent.  
**MoveCategoriesAndMacros**|  Moves child categories and macros to the category's parent.  
**None**|  Delete a single specification macro category with no children.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.DeleteMacroCategoryBehavior**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks Namespace](topic2159.md)



Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectCalculationTableColumnType Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectCalculationTableColumnType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

A set of different types of calculation table columns. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum ProjectCalculationTableColumnType 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumnType](topic2356.md)  
  
C#|   
---|---  
      
    
    public enum ProjectCalculationTableColumnType : System.Enum   
  
# Members

Member| Description  
---|---  
**ControlInput**|  Column's cell values are fetched from controls with the same names as the cells.  
**ControlOutput**|  The values from the cells can be automatically bound into matching controls with the same name.  
**Data**|  Default type with no special behaviours.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.ProjectCalculationTableColumnType**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks Namespace](topic2159.md)



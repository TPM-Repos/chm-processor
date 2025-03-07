Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MacroConsistencyLevel Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : MacroConsistencyLevel Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines the required consistency level of the macro. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum MacroConsistencyLevel 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [MacroConsistencyLevel](topic10769.md)  
  
C#|   
---|---  
      
    
    public enum MacroConsistencyLevel : System.Enum   
  
# Members

Member| Description  
---|---  
**Full**|  The specification must be in a fully consistent state before the macro can be executed.  
**None**|  No consistency is required for the macro to be callable.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Specification.MacroConsistencyLevel**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Specification Namespace](topic10764.md)



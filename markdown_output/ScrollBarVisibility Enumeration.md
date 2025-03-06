       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ScrollBarVisibility Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : ScrollBarVisibility Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The visibility style of a scroll bar. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum ScrollBarVisibility 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ScrollBarVisibility](topic7316.md)  
  
C#|   
---|---  
      
    
    public enum ScrollBarVisibility : System.Enum   
  
# Members

Member| Description  
---|---  
**Auto**|  The scroll bar will shown when needed, but is otherwise hidden.  
**Default**|  The scroll bar visibility has not been explicitly set and a default fallback value will be applied.  
**Hidden**|  The scroll bar is always hidden and scrolling is disabled.  
**Visible**|  The scroll bar is visible at all times, but is disabled when not needed.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Forms.ScrollBarVisibility**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Forms Namespace](topic7266.md)



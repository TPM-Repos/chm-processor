Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvalidNumberHandling Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) : InvalidNumberHandling Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Controls the way invalid values such as System.Double and System.Double will get handled in a [DynamicProperty](topic9398.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum InvalidNumberHandling 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [InvalidNumberHandling](topic9382.md)  
  
C#|   
---|---  
      
    
    public enum InvalidNumberHandling : System.Enum   
  
# Members

Member| Description  
---|---  
**AllowInvalidValues**|  Invalid numbers are allowed.  
**ResetToDefault**|  Invalid values will be set to the default value of the [DynamicProperty](topic9398.md).  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Forms.DataModel.InvalidNumberHandling**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Forms.DataModel Namespace](topic9371.md)



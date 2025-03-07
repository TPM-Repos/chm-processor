Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MergedItemState Enumeration   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : MergedItemState Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the state of a merged item. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum MergedItemState 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [MergedItemState](topic13453.md)  
  
C#|   
---|---  
      
    
    public enum MergedItemState : System.Enum   
  
# Members

Member| Description  
---|---  
**Captured**|  The item is captured (exists in SolidWorks and in DriveWorks).  
**Deleted**|  The item is deleted (exists in DriveWorks but not in SolidWorks).  
**NotCaptured**|  The item is not captured (exists in SolidWorks, but not in DriveWorks).  
**Unknown**|  The item is in an unknown state because neither a SolidWorks nor DriveWorks object have been set.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.SolidWorks.MergedItemState**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.SolidWorks Namespace](topic13345.md)



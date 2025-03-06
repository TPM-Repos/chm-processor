RuleSection Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : RuleSection Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents a part of DriveWorks containing rules. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <FlagsAttribute()>
    Public Enum RuleSection 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleSection](topic2362.md)  
  
C#|   
---|---  
      
    
    [FlagsAttribute()]
    public enum RuleSection : System.Enum   
  
# Members

Member| Description  
---|---  
**All**|  All areas of DriveWorks containing rules.  
**CalculationTables**|  Calculation Table Cells.  
**ComponentSets**|  The Model And Drawing rules view.  
**ComponentTasks**|  The component tasks.  
**Controls**|  The dynamic properties of Form Controls.  
**Decisions**|  Decisions in the Specification Flow.  
**Documents**|  The Documents view.  
**Messages**|  The project messages view.  
**SpecificationFlow**|  Specification Flow Tasks.  
**SpecificationMacros**|  Specification Macros.  
**SpecificationProperties**|  The project specification properties.  
**SpecificationSetting**|  The Specification Settings view.  
**Variables**|  The Variables view.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.RuleSection**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks Namespace](topic2159.md)



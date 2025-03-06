![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleSection Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2362.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : RuleSection Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents a part of DriveWorks containing rules. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <FlagsAttribute()>
    Public Enum RuleSection 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RuleSection](topic2362.md)  
  
C#|   
---|---  
      
    
    [FlagsAttribute()]
    public enum RuleSection : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

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
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.RuleSection**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.

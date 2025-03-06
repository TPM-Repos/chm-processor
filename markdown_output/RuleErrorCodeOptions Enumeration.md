![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleErrorCodeOptions Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2361.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : RuleErrorCodeOptions Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets known rule evaluation error codes. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum RuleErrorCodeOptions 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RuleErrorCodeOptions](topic2361.md)  
  
C#|   
---|---  
      
    
    public enum RuleErrorCodeOptions : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**Calculation**|  The value couldn't be calculated (this is a DriveWorks defined error code.)  
**CircularReference**|  The value couldn't be calculated because the rule is circular (this is a DriveWorks defined error code.)  
**DivisionByZero**|  An attempt was made to divide by zero.  
**InvalidRule**|  The value couldn't be calculated because the rule is invalid (this is a DriveWorks defined error code.)  
**Name**|  A name used in the rule or one or more of its dependants is invalid.  
**NotApplicable**|  A performed operation was invalid.  
**Null**|  An attempt is made to use a null value.  
**Number**|   
**RecursionLimitReached**|  The value couldn't be calculated because the calculation hits a recursive depth exceeding the recursion limit (this is a DriveWorks defined error code.)  
**Reference**|  A referenced cell is invalid.  
**Value**|  The value is invalid or out of range.  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.RuleErrorCodeOptions**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.

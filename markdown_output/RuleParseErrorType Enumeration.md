![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleParseErrorType Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10557.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) : RuleParseErrorType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the type of error from a rule. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum RuleParseErrorType 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RuleParseErrorType](topic10557.md)  
  
C#|   
---|---  
      
    
    public enum RuleParseErrorType : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**ExpectedBeginParanthesis**|  A starting paranthesis was not found at an expected location.  
**ExpectedEndParanthesis**|  An ending paranthesis was not found at the expected location.  
**ExpectedName**|  A name was not found at an expected location.  
**ExpectedSeperatorOrEndOfFunction**|  A list separator or ending-paranthesis was not found at the expected location in a function call.  
**PrematureEndOfRule**|  The token stream was empty when more tokens where expected.  
**SyntaxError**|  A syntax error was encountered.  
**TailingTokens**|  The token stream contains unexpected trailing tokens.  
**UnexpectedToken**|  An unexpected token was found.  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Rules.RuleParseErrorType**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.Rules Namespace](topic10510.md)

©2024 DriveWorks Ltd. All Rights Reserved.

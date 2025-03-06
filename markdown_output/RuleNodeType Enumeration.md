![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleNodeType Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10556.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) : RuleNodeType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the type of a node in an abstract syntax tree for a rule. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum RuleNodeType 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RuleNodeType](topic10556.md)  
  
C#|   
---|---  
      
    
    public enum RuleNodeType : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**ArgumentSeparator**|  The node represents a separator between two arguments to a function call.  
**BooleanValue**|  The node represents a literal boolean value.  
**CloseBrace**|  The node represents a closing brace.  
**CloseParanthesis**|  The node represents a closing paranthesis.  
**Empty**|  The node type is not specified.  
**FormattedString**|  The node represents a formatted string.  
**FormattedStringContent**|  The node represents a string segment of a formatted string node.  
**FormattedStringRule**|  The node represents a rule segment of a formatted string node.  
**FunctionCall**|  The node represents a function call.  
**Invalid**|  The node is invalid.  
**LambdaFunction**|  The node represents a generic rule node passed into anonymous functions.  
**LambdaReference**|  The node represents an anonymous reference in a Lambda function.  
**ListOfListsSeparator**|  The node represents a list of lists separator.  
**LiteralArray**|  The node represents a literal array or table.  
**NumberValue**|  The node represents a literal numeric value.  
**OpenBrace**|  The node represents an opening brace.  
**OpenParanthesis**|  The node represents an opening paranthesis.  
**Operation**|  The node represents an operator.  
**PotentialLambda**|  The node represents where there is ambiguity between whether a new Lambda Parameter is being defined, or a LambdaFunction is being written.  
**Reference**|  The node represents a reference to a named item.  
**RelativeReference**|  The node represents a relative reference to an adjacent item.  
**StringValue**|  The node represents a literal string value.  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Rules.RuleNodeType**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.Rules Namespace](topic10510.md)

©2024 DriveWorks Ltd. All Rights Reserved.

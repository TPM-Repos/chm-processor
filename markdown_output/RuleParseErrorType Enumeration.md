       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleParseErrorType Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) : RuleParseErrorType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the type of error from a rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum RuleParseErrorType 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleParseErrorType](topic10557.md)  
  
C#|   
---|---  
      
    
    public enum RuleParseErrorType : System.Enum   
  
# Members

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
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Rules.RuleParseErrorType**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Rules Namespace](topic10510.md)



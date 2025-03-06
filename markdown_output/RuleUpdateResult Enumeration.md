RuleUpdateResult Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Localization Namespace](topic10015.md) : RuleUpdateResult Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Indicates the result of a method which changes a rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum RuleUpdateResult 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleUpdateResult](topic10017.md)  
  
C#|   
---|---  
      
    
    public enum RuleUpdateResult : System.Enum   
  
# Members

Member| Description  
---|---  
**Invalid**|  The rule couldn't be parsed successfully.  
**NotApplicable**|  There were no changes to be made.  
**NotRule**|  The specified value wasn't a rule.  
**Success**|  The rule was updated successfully.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Localization.RuleUpdateResult**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Localization Namespace](topic10015.md)



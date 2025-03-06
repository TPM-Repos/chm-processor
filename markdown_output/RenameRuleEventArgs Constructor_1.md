       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RenameRuleEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10313.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameRuleEventArgs Class](topic10306.md) : RenameRuleEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_containerName_
    The name of the rule container.

_ruleName_
    The name of the rule in a format specific to the type of container.

_ruleText_
    The rule text.

Glossary Item Box

Initializes a new instance of the [RenameRuleEventArgs](topic10306.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _containerName_ As String, _
       ByVal _ruleName_ As String, _
       ByVal _ruleText_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim containerName As String
    Dim ruleName As String
    Dim ruleText As String
     
    Dim instance As New [RenameRuleEventArgs](topic10306.md)(containerName, ruleName, ruleText)  
  
C#|   
---|---  
      
    
    public RenameRuleEventArgs( 
       string _containerName_ ,
       string _ruleName_ ,
       string _ruleText_
    )  
  
#### Parameters

 _containerName_
    The name of the rule container.
_ruleName_
    The name of the rule in a format specific to the type of container.
_ruleText_
    The rule text.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RenameRuleEventArgs Class](topic10306.md)   
[RenameRuleEventArgs Members](topic10307.md)

©2024 DriveWorks Ltd. All Rights Reserved.

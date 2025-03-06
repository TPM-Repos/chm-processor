       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RenderHelp Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1589.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.RulesBuilder Namespace](topic1581.md) > [IRuleHelpProvider Interface](topic1583.md) : RenderHelp Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleType_
    The type of rule which matched one of the supported rule types returned by [GetSupportedRuleTypes](topic1588.md).

_temporaryPath_
    The full path to a temporary directory into which the HTML and any supporting files should be copied.

Glossary Item Box

Renders the help for the given rule type to the specified temporary directory, and returns the full path to the HTML file which will be shown in the rules builder help pane. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RenderHelp( _
       ByVal _ruleType_ As String, _
       ByVal _temporaryPath_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IRuleHelpProvider](topic1583.md)
    Dim ruleType As String
    Dim temporaryPath As String
    Dim value As String
     
    value = instance.RenderHelp(ruleType, temporaryPath)  
  
C#|   
---|---  
      
    
    string RenderHelp( 
       string _ruleType_ ,
       string _temporaryPath_
    )  
  
#### Parameters

 _ruleType_
    The type of rule which matched one of the supported rule types returned by [GetSupportedRuleTypes](topic1588.md).
_temporaryPath_
    The full path to a temporary directory into which the HTML and any supporting files should be copied.

#### Return Value

The full path to the rendered HTML file.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IRuleHelpProvider Interface](topic1583.md)   
[IRuleHelpProvider Members](topic1584.md)

©2024 DriveWorks Ltd. All Rights Reserved.

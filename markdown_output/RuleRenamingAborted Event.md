![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleRenamingAborted Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10300.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameProcess Class](topic10287.md) : RuleRenamingAborted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised if the processing of an individual rule is aborted, e.g. because it can't be parsed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event RuleRenamingAborted As EventHandler(Of RenameRuleEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RenameProcess](topic10287.md)
    Dim handler As EventHandler(Of RenameRuleEventArgs)
     
    AddHandler instance.RuleRenamingAborted, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<RenameRuleEventArgs> RuleRenamingAborted  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [RenameRuleEventArgs](topic10306.md) containing data related to this event. The following **RenameRuleEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ContainerName](topic10314.md)| Gets the name of the rule container.   
[RuleName](topic10315.md)| Gets the name of the rule in a format specific to the type of container.   
[RuleText](topic10316.md)| Gets the text of the rule.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RenameProcess Class](topic10287.md)   
[RenameProcess Members](topic10288.md)

©2024 DriveWorks Ltd. All Rights Reserved.

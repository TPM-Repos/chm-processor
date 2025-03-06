![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryTranslateRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10031.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Localization Namespace](topic10015.md) > [RuleLocalizationHelper Class](topic10018.md) : TryTranslateRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_originalRuleText_
    The rule to translate.

_translatedRuleText_
    Receives the translated rule.

_sourceLanguage_
    The culture which defines the language the rule was written in.

_sourceFormatting_
    The culture which defines the formatting used for the rule was written in.

Glossary Item Box

Translates the given rule from the provided language into the language represented by the instance. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryTranslateRule( _
       ByVal _originalRuleText_ As String, _
       ByRef _translatedRuleText_ As String, _
       ByVal _sourceLanguage_ As CultureInfo, _
       ByVal _sourceFormatting_ As CultureInfo _
    ) As [RuleUpdateResult](topic10017.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RuleLocalizationHelper](topic10018.md)
    Dim originalRuleText As String
    Dim translatedRuleText As String
    Dim sourceLanguage As CultureInfo
    Dim sourceFormatting As CultureInfo
    Dim value As [RuleUpdateResult](topic10017.md)
     
    value = instance.TryTranslateRule(originalRuleText, translatedRuleText, sourceLanguage, sourceFormatting)  
  
C#|   
---|---  
      
    
    public [RuleUpdateResult](topic10017.md) TryTranslateRule( 
       string _originalRuleText_ ,
       ref string _translatedRuleText_ ,
       CultureInfo _sourceLanguage_ ,
       CultureInfo _sourceFormatting_
    )  
  
#### Parameters

 _originalRuleText_
    The rule to translate.
_translatedRuleText_
    Receives the translated rule.
_sourceLanguage_
    The culture which defines the language the rule was written in.
_sourceFormatting_
    The culture which defines the formatting used for the rule was written in.

#### Return Value

A value indicating whether the translation was successful.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RuleLocalizationHelper Class](topic10018.md)   
[RuleLocalizationHelper Members](topic10019.md)

©2024 DriveWorks Ltd. All Rights Reserved.

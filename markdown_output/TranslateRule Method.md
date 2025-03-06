       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TranslateRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10030.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Localization Namespace](topic10015.md) > [RuleLocalizationHelper Class](topic10018.md) : TranslateRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_originalRuleText_
    The rule to translate.

_sourceLanguage_
    The culture which defines the language the rule was written in.

_sourceFormatting_
    The culture which defines the formatting used for the rule was written in.

Glossary Item Box

Translates the given rule from the provided language into the language represented by the instance. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TranslateRule( _
       ByVal _originalRuleText_ As String, _
       ByVal _sourceLanguage_ As CultureInfo, _
       ByVal _sourceFormatting_ As CultureInfo _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleLocalizationHelper](topic10018.md)
    Dim originalRuleText As String
    Dim sourceLanguage As CultureInfo
    Dim sourceFormatting As CultureInfo
    Dim value As String
     
    value = instance.TranslateRule(originalRuleText, sourceLanguage, sourceFormatting)  
  
C#|   
---|---  
      
    
    public string TranslateRule( 
       string _originalRuleText_ ,
       CultureInfo _sourceLanguage_ ,
       CultureInfo _sourceFormatting_
    )  
  
#### Parameters

 _originalRuleText_
    The rule to translate.
_sourceLanguage_
    The culture which defines the language the rule was written in.
_sourceFormatting_
    The culture which defines the formatting used for the rule was written in.

#### Return Value

The translated rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleLocalizationHelper Class](topic10018.md)   
[RuleLocalizationHelper Members](topic10019.md)

©2024 DriveWorks Ltd. All Rights Reserved.

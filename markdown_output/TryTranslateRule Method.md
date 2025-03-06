TryTranslateRule Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryTranslateRule( _
       ByVal _originalRuleText_ As String, _
       ByRef _translatedRuleText_ As String, _
       ByVal _sourceLanguage_ As CultureInfo, _
       ByVal _sourceFormatting_ As CultureInfo _
    ) As [RuleUpdateResult](topic10017.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleLocalizationHelper Class](topic10018.md)   
[RuleLocalizationHelper Members](topic10019.md)



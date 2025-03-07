Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetLocalizedName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RuleSectionUtility Class](topic5269.md) : GetLocalizedName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_section_
    The value to get the localized string of.

Glossary Item Box

Gets the localized name of the specified enum. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetLocalizedName( _
       ByVal _section_ As [RuleSection](topic2362.md) _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim section As [RuleSection](topic2362.md)
    Dim value As String
     
    value = [RuleSectionUtility](topic5269.md).GetLocalizedName(section)  
  
C#|   
---|---  
      
    
    public static string GetLocalizedName( 
       [RuleSection](topic2362.md) _section_
    )  
  
#### Parameters

 _section_
    The value to get the localized string of.

#### Return Value

The localized name of the value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleSectionUtility Class](topic5269.md)   
[RuleSectionUtility Members](topic5270.md)



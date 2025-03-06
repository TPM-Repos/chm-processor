       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleLocalizationHelper Constructor(CultureInfo,String,String,String)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10025.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Localization Namespace](topic10015.md) > [RuleLocalizationHelper Class](topic10018.md) > [RuleLocalizationHelper Constructor](topic10024.md) : RuleLocalizationHelper Constructor(CultureInfo,String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_localizationCulture_
    The culture for which to initialize the localization helper.

_listSeparator_
    The list separator to use for formatting.

_decimalSeparator_
    The decimal separator to use for formatting.

_thousandsSeparator_
    The thousands separator to use for formatting.

Glossary Item Box

Initializes a new instance of the [RuleLocalizationHelper](topic10018.md) type for the given culture. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _localizationCulture_ As CultureInfo, _
       ByVal _listSeparator_ As String, _
       ByVal _decimalSeparator_ As String, _
       ByVal _thousandsSeparator_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim localizationCulture As CultureInfo
    Dim listSeparator As String
    Dim decimalSeparator As String
    Dim thousandsSeparator As String
     
    Dim instance As New [RuleLocalizationHelper](topic10018.md)(localizationCulture, listSeparator, decimalSeparator, thousandsSeparator)  
  
C#|   
---|---  
      
    
    public RuleLocalizationHelper( 
       CultureInfo _localizationCulture_ ,
       string _listSeparator_ ,
       string _decimalSeparator_ ,
       string _thousandsSeparator_
    )  
  
#### Parameters

 _localizationCulture_
    The culture for which to initialize the localization helper.
_listSeparator_
    The list separator to use for formatting.
_decimalSeparator_
    The decimal separator to use for formatting.
_thousandsSeparator_
    The thousands separator to use for formatting.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleLocalizationHelper Class](topic10018.md)   
[RuleLocalizationHelper Members](topic10019.md)   
[Overload List](topic10024.md)

©2024 DriveWorks Ltd. All Rights Reserved.

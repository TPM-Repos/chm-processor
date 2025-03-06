![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddHelpProvider Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1603.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.RulesBuilder Namespace](topic1581.md) > [IRulesBuilderService Interface](topic1598.md) : AddHelpProvider Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_provider_
    The provider to add.

Glossary Item Box

Adds an inline help provider. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub AddHelpProvider( _
       ByVal _provider_ As [IRuleHelpProvider](topic1583.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IRulesBuilderService](topic1598.md)
    Dim provider As [IRuleHelpProvider](topic1583.md)
     
    instance.AddHelpProvider(provider)  
  
C#|   
---|---  
      
    
    void AddHelpProvider( 
       [IRuleHelpProvider](topic1583.md) _provider_
    )  
  
#### Parameters

 _provider_
    The provider to add.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IRulesBuilderService Interface](topic1598.md)   
[IRulesBuilderService Members](topic1599.md)

©2024 DriveWorks Ltd. All Rights Reserved.

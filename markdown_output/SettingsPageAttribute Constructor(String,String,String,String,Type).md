       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SettingsPageAttribute Constructor(String,String,String,String,Type)   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SettingsPageAttribute Class](topic959.md) > [SettingsPageAttribute Constructor](topic965.md) : SettingsPageAttribute Constructor(String,String,String,String,Type)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_invariantName_
    The non-localized name of the settings page.

_displayName_
    The display name of the settings page.

_description_
    The description of the settings page.

_imageResourceName_
    The name of the resource containing the page's image in the form "#ResourceManifestName,ImageResourceName", e.g. "#MyAssembly.LocalizedResources,MySettingsPageImage".

_pageType_
    The CLR type of the control which implements the settings page.

Glossary Item Box

Initializes a new instance of the [SettingsPageAttribute](topic959.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _invariantName_ As String, _
       ByVal _displayName_ As String, _
       ByVal _description_ As String, _
       ByVal _imageResourceName_ As String, _
       ByVal _pageType_ As Type _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim invariantName As String
    Dim displayName As String
    Dim description As String
    Dim imageResourceName As String
    Dim pageType As Type
     
    Dim instance As New [SettingsPageAttribute](topic959.md)(invariantName, displayName, description, imageResourceName, pageType)  
  
C#|   
---|---  
      
    
    public SettingsPageAttribute( 
       string _invariantName_ ,
       string _displayName_ ,
       string _description_ ,
       string _imageResourceName_ ,
       Type _pageType_
    )  
  
#### Parameters

 _invariantName_
    The non-localized name of the settings page.
_displayName_
    The display name of the settings page.
_description_
    The description of the settings page.
_imageResourceName_
    The name of the resource containing the page's image in the form "#ResourceManifestName,ImageResourceName", e.g. "#MyAssembly.LocalizedResources,MySettingsPageImage".
_pageType_
    The CLR type of the control which implements the settings page.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SettingsPageAttribute Class](topic959.md)   
[SettingsPageAttribute Members](topic960.md)   
[Overload List](topic965.md)



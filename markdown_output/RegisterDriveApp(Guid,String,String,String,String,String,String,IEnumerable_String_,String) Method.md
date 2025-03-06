![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterDriveApp(Guid,String,String,String,String,String,String,IEnumerable<String>,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) > [RegisterDriveApp Method](topic3215.md) : RegisterDriveApp(Guid,String,String,String,String,String,String,IEnumerable<String>,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppId_
    The unique identifier of the DriveApp.

_name_
    The name of the DriveApp.

_appAlias_
    The alias name of the DriveApp.

_defaultProjectName_
    The name of the default project that the DriveApp will run.

_connectionString_
    The connection string of the database to use with the DriveApp.

_startParameter_
    The start parameter to use when running the DriveApp.

_driveAppPath_
    The path of the DriveApp directory.

_projectPaths_
    The full paths of the projects contained within the DriveApp directory including subdirectories.

_version_
    The driveApp version.

Glossary Item Box

Registers a DriveApp in the group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function RegisterDriveApp( _
       ByVal _driveAppId_ As Guid, _
       ByVal _name_ As String, _
       ByVal _appAlias_ As String, _
       ByVal _defaultProjectName_ As String, _
       ByVal _connectionString_ As String, _
       ByVal _startParameter_ As String, _
       ByVal _driveAppPath_ As String, _
       ByVal _projectPaths_ As IEnumerable(Of String), _
       ByVal _version_ As String _
    ) As [DriveAppDetails](topic2750.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppId As Guid
    Dim name As String
    Dim appAlias As String
    Dim defaultProjectName As String
    Dim connectionString As String
    Dim startParameter As String
    Dim driveAppPath As String
    Dim projectPaths As IEnumerable(Of String)
    Dim version As String
    Dim value As [DriveAppDetails](topic2750.md)
     
    value = instance.RegisterDriveApp(driveAppId, name, appAlias, defaultProjectName, connectionString, startParameter, driveAppPath, projectPaths, version)  
  
C#|   
---|---  
      
    
    public [DriveAppDetails](topic2750.md) RegisterDriveApp( 
       Guid _driveAppId_ ,
       string _name_ ,
       string _appAlias_ ,
       string _defaultProjectName_ ,
       string _connectionString_ ,
       string _startParameter_ ,
       string _driveAppPath_ ,
       IEnumerable<string> _projectPaths_ ,
       string _version_
    )  
  
#### Parameters

 _driveAppId_
    The unique identifier of the DriveApp.
_name_
    The name of the DriveApp.
_appAlias_
    The alias name of the DriveApp.
_defaultProjectName_
    The name of the default project that the DriveApp will run.
_connectionString_
    The connection string of the database to use with the DriveApp.
_startParameter_
    The start parameter to use when running the DriveApp.
_driveAppPath_
    The path of the DriveApp directory.
_projectPaths_
    The full paths of the projects contained within the DriveApp directory including subdirectories.
_version_
    The driveApp version.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)   
[Overload List](topic3215.md)



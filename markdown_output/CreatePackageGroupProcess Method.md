Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreatePackageGroupProcess Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [PackageGroupProcess Class](topic9925.md) : CreatePackageGroupProcess Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceGroup_
    The group to copy from.

_packagePath_
    the path of the package file to create.

_targetGroupName_
    The name of the group to create inside the package.

_options_
    The options to use to pack the group.

Glossary Item Box

Creates a new instance of the [PackageGroupProcess](topic9925.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function CreatePackageGroupProcess( _
       ByVal _sourceGroup_ As [Group](topic2958.md), _
       ByVal _packagePath_ As String, _
       ByVal _targetGroupName_ As String, _
       ByVal _options_ As [CopyGroupOptions](topic9736.md) _
    ) As [PackageGroupProcess](topic9925.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim sourceGroup As [Group](topic2958.md)
    Dim packagePath As String
    Dim targetGroupName As String
    Dim options As [CopyGroupOptions](topic9736.md)
    Dim value As [PackageGroupProcess](topic9925.md)
     
    value = [PackageGroupProcess](topic9925.md).CreatePackageGroupProcess(sourceGroup, packagePath, targetGroupName, options)  
  
C#|   
---|---  
      
    
    public static [PackageGroupProcess](topic9925.md) CreatePackageGroupProcess( 
       [Group](topic2958.md) _sourceGroup_ ,
       string _packagePath_ ,
       string _targetGroupName_ ,
       [CopyGroupOptions](topic9736.md) _options_
    )  
  
#### Parameters

 _sourceGroup_
    The group to copy from.
_packagePath_
    the path of the package file to create.
_targetGroupName_
    The name of the group to create inside the package.
_options_
    The options to use to pack the group.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PackageGroupProcess Class](topic9925.md)   
[PackageGroupProcess Members](topic9926.md)



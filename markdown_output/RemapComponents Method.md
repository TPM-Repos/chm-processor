       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemapComponents Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) : RemapComponents Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldBasePath_
    The base path from which all changes must match.

_newBasePath_
    The new base path to give all matching components.

Glossary Item Box

Attempts to change all captured components and their references that match oldBasePath to use the new base path in newBasePath. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RemapComponents( _
       ByVal _oldBasePath_ As String, _
       ByVal _newBasePath_ As String _
    ) As IReadOnlyDictionary(Of String,String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim oldBasePath As String
    Dim newBasePath As String
    Dim value As IReadOnlyDictionary(Of String,String)
     
    value = instance.RemapComponents(oldBasePath, newBasePath)  
  
C#|   
---|---  
      
    
    public IReadOnlyDictionary<string,string> RemapComponents( 
       string _oldBasePath_ ,
       string _newBasePath_
    )  
  
#### Parameters

 _oldBasePath_
    The base path from which all changes must match.
_newBasePath_
    The new base path to give all matching components.

#### Return Value

A mapping of all old paths to new paths.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)



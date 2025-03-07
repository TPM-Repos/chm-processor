Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeserializeConfiguration Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupOptionsSerializer Class](topic9768.md) : DeserializeConfiguration Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceGroup_
    The group that is currently in use.

_configurationPath_
    The location of the configuration to use.

Glossary Item Box

Deserializes an XML file containing a configuration for a Copy Group or Pack and Go process. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function DeserializeConfiguration( _
       ByVal _sourceGroup_ As [Group](topic2958.md), _
       ByVal _configurationPath_ As String _
    ) As [CopyGroupConfigurationResult](topic9719.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim sourceGroup As [Group](topic2958.md)
    Dim configurationPath As String
    Dim value As [CopyGroupConfigurationResult](topic9719.md)
     
    value = [CopyGroupOptionsSerializer](topic9768.md).DeserializeConfiguration(sourceGroup, configurationPath)  
  
C#|   
---|---  
      
    
    public static [CopyGroupConfigurationResult](topic9719.md) DeserializeConfiguration( 
       [Group](topic2958.md) _sourceGroup_ ,
       string _configurationPath_
    )  
  
#### Parameters

 _sourceGroup_
    The group that is currently in use.
_configurationPath_
    The location of the configuration to use.

#### Return Value

Returns an instance of [CopyGroupConfigurationResult](topic9719.md) based on the configuration file used.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.CopyGroupOptionsSerializerException](topic2615.md)| A problem occurred deserializing the configuration file, check the System.Exception.InnerException for more detail.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CopyGroupOptionsSerializer Class](topic9768.md)   
[CopyGroupOptionsSerializer Members](topic9769.md)



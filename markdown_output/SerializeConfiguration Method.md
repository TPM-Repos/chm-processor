       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SerializeConfiguration Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9775.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupOptionsSerializer Class](topic9768.md) : SerializeConfiguration Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_options_
    A set of selected options for copying group information.

Glossary Item Box

Serialize the values of the CopyGroupOptions to XML to be used as a configuration for 'Copy Group' and 'Pack and Go' processes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function SerializeConfiguration( _
       ByVal _options_ As [CopyGroupOptions](topic9736.md) _
    ) As XDocument  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim options As [CopyGroupOptions](topic9736.md)
    Dim value As XDocument
     
    value = [CopyGroupOptionsSerializer](topic9768.md).SerializeConfiguration(options)  
  
C#|   
---|---  
      
    
    public static XDocument SerializeConfiguration( 
       [CopyGroupOptions](topic9736.md) _options_
    )  
  
#### Parameters

 _options_
    A set of selected options for copying group information.

#### Return Value

Returns the values for the provided CopyGroupOptions as XML.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CopyGroupOptionsSerializer Class](topic9768.md)   
[CopyGroupOptionsSerializer Members](topic9769.md)

©2024 DriveWorks Ltd. All Rights Reserved.

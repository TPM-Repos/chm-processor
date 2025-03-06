RequestElevation Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) : RequestElevation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Requests elevation if supported. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RequestElevation() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim value As Boolean
     
    value = instance.RequestElevation()  
  
C#|   
---|---  
      
    
    bool RequestElevation()  
  
#### Return Value

True if the request for elevation successfully results in elevation, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)



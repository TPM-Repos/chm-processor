![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ILibraryInfo Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2055.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) : ILibraryInfo Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ILibraryInfo](topic2055.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [Assembly](topic2065.md)| Gets the assembly if it is loaded, or a null reference otherwise.   
![ Property](dotnetimages/Property.gif)| [Description](topic2066.md)| Gets the localized description of the library.   
![ Property](dotnetimages/Property.gif)| [DisplayName](topic2067.md)| Gets the display name of the assembly directly from the assembly if it has been loaded, otherwise from the fallback display name.   
![ Property](dotnetimages/Property.gif)| [ExtensionTypes](topic2068.md)| Gets the extension types in the assembly.   
![ Property](dotnetimages/Property.gif)| [FallbackDisplayName](topic2069.md)| Gets the display name of the assembly from its registered information.   
![ Property](dotnetimages/Property.gif)| [InvariantName](topic2070.md)| Gets the invariant name of the extension library.   
![ Property](dotnetimages/Property.gif)| [IsFrameworkLibrary](topic2071.md)| Determines whether the library is a framework library.   
![ Property](dotnetimages/Property.gif)| [LastLoadException](topic2072.md)| If an exception occurred loading the extension library, this property will retrieve the exception.   
![ Property](dotnetimages/Property.gif)| [LastTypeLoadException](topic2073.md)| If an exception occurred loading the extension library's types, this property will retrieve the exception.   
![ Property](dotnetimages/Property.gif)| [LoadOnStartup](topic2074.md)| Determines whether the library is loaded on start up.   
![ Property](dotnetimages/Property.gif)| [Location](topic2075.md)| Gets the location of the library.   
![ Property](dotnetimages/Property.gif)| [Publisher](topic2076.md)| Gets the name of the library publisher.   
![ Property](dotnetimages/Property.gif)| [PublisherUrl](topic2077.md)| Gets a URL pointing to a web site for the library or its publisher.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [GetExtensibilityAttributes](topic2060.md)| Overloaded. Gets the extensibility attributes for the library.   
![ Method](dotnetimages/Method.gif)| [Load](topic2064.md)| Loads the library if it hasn't already been loaded.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [Loaded](topic2078.md)| Occurs when the library is loaded.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ILibraryInfo Interface](topic2055.md)   
[DriveWorks.Applications.Extensibility Namespace](topic1995.md)

©2024 DriveWorks Ltd. All Rights Reserved.
